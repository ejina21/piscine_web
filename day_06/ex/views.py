from django.shortcuts import render
from django.views.generic import TemplateView, CreateView, DeleteView, View

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
            tip = context["form"].save(commit=False)
            tip.author = request.user
            tip.save()
        return super(TemplateView, self).render_to_response(context)

    def get_context_data(self, **kwargs):
        context = super(HomePageView, self).get_context_data(**kwargs)
        form = TipForm(self.request.POST or None)
        elements = Tip.objects.all()
        context['elements'] = elements
        context['form'] = form
        context['message'] = kwargs['message'] if 'message' in kwargs else ''
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


class DeleteTipView(LoginRequiredMixin, View):
    login_url = 'login'

    def get(self, request, *args, **kwargs):
        tip = Tip.objects.get(pk=kwargs['pk'])
        if tip.author == request.user or request.user.is_staff \
                or request.user.is_superuser or request.user.profileuser.reputation >= 30:
            plus = tip.positive * 5
            minus = tip.negative * 2
            summary = minus - plus
            tip.author.profileuser.reputation += summary
            tip.author.save()
            tip.delete()

        return HttpResponseRedirect(reverse_lazy('home'))


class UpvoteView(LoginRequiredMixin, View):
    login_url = 'login'

    def get(self, request, *args, **kwargs):
        tip = Tip.objects.get(pk=kwargs['pk'])
        up = Upvote.objects.filter(
            tip=tip,
            user=request.user,
        )
        if up.exists():
            tip.positive -= 1
            tip.author.profileuser.reputation -= 5
            tip.author.save()
            up.delete()
        else:
            Upvote.objects.create(
                tip=tip,
                user=request.user,
            )
            tip.positive += 1
            tip.author.profileuser.reputation += 5
            tip.author.save()
        tip.save()
        return HttpResponseRedirect(reverse_lazy('home'))


class DownvoteView(LoginRequiredMixin, View):
    login_url = 'login'

    def get(self, request, *args, **kwargs):
        tip = Tip.objects.get(pk=kwargs['pk'])
        if tip.author == request.user or request.user.is_staff \
                or request.user.is_superuser or request.user.profileuser.reputation >= 15:
            down = Downvote.objects.filter(
                tip=tip,
                user=request.user,
            )
            if down.exists():
                tip.negative -= 1
                tip.author.profileuser.reputation += 2
                tip.author.save()
                down.delete()
            else:
                Downvote.objects.create(
                    tip=tip,
                    user=request.user,
                )
                tip.negative += 1
                tip.author.profileuser.reputation -= 2
                tip.author.save()
            tip.save()
        return HttpResponseRedirect(reverse_lazy('home'))
