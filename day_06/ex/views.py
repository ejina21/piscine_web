from django.shortcuts import render
from django.views.generic import TemplateView, CreateView, DeleteView, View

from day_06.settings import USER_NAMES
from ex.forms import UserCreationForm, TipForm
from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from ex.models import Tip, Upvote, Downvote
from django.contrib.auth.mixins import LoginRequiredMixin


class HomePageView(TemplateView):
    template_name = 'home.html'

    def post(self, request, *args, **kwargs):
        context = self.get_context_data()
        if context["form"].is_valid():
            context["form"].save()
        return super(TemplateView, self).render_to_response(context)

    def get_context_data(self, **kwargs):
        context = super(HomePageView, self).get_context_data(**kwargs)
        form = TipForm(self.request.POST or None)
        elements = Tip.objects.all()
        context['elements'] = elements
        context['form'] = form
        return context


class SignUpView(CreateView):
    form_class = UserCreationForm
    template_name = 'signup.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            new_user = form.save(commit=False)
            new_user.set_password(form.cleaned_data['password'])
            new_user.save()
            return HttpResponseRedirect(reverse('login'))
        return render(request, self.template_name, {'form': form})


class DeleteTipView(LoginRequiredMixin, DeleteView):
    model = Tip
    template_name = 'remove.html'
    login_url = 'login'
    success_url = reverse_lazy('home')


class UpvoteView(View):
    def get(self, request, *args, **kwargs):
        tip = Tip.objects.get(pk=kwargs['pk'])
        up = Upvote.objects.filter(
            tip=tip,
            user=request.user,
        )
        if up.exists():
            tip.positive -= 1
            up.delete()
        else:
            Upvote.objects.create(
                tip=tip,
                user=request.user,
            )
            tip.positive += 1
        tip.save()
        return HttpResponseRedirect(reverse_lazy('home'))


class DownvoteView(View):
    def get(self, request, *args, **kwargs):
        tip = Tip.objects.get(pk=kwargs['pk'])
        down = Downvote.objects.filter(
            tip=tip,
            user=request.user,
        )
        if down.exists():
            tip.negative -= 1
            down.delete()
        else:
            Downvote.objects.create(
                tip=tip,
                user=request.user,
            )
            tip.negative += 1
        tip.save()
        return HttpResponseRedirect(reverse_lazy('home'))
