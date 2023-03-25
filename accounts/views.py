from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect
from django.views.generic import TemplateView, CreateView
from accounts.forms import (
    LoginForm,
    CustomUserCreationForm,
)


class LoginView(TemplateView):
    template_name = 'login.html'
    form = LoginForm

    def get(self, request, *args, **kwargs):
        form = self.form()
        context = {'form': form}
        return self.render_to_response(context)

    def post(self, request, *args, **kwargs):
        form = self.form(request.POST)
        if not form.is_valid():
            messages.error(request, 'Некорректная форма')
            return redirect('reviewer:index')
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(request, username=username, password=password)
        if not user:
            messages.warning(request, 'Пользователь не найден')
            return redirect('reviewer:index')
        login(request, user)
        messages.success(request, 'Добро пожаловать')
        next = request.GET.get('next')
        if next:
            return redirect(next)
        return redirect('reviewer:index')


def logout_view(request):
    logout(request)
    return redirect("reviewer:index")


class RegisterView(CreateView):
    template_name = "register.html"
    form_class = CustomUserCreationForm
    success_url = "/"

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect(self.success_url)
        context = {"form": form}
        return self.render_to_response(context)

# class UserDetailView(LoginRequiredMixin, DetailView):
#     model = get_user_model()
#     template_name = 'user_detail.html'
#     context_object_name = 'user_obj'
#     paginate_related_by = 5
#     paginate_related_orphans = 0
#
#     def get_context_data(self, **kwargs):
#         articles = self.object.articles.order_by('-created_at')
#         paginator = Paginator(articles, self.paginate_related_by, orphans=self.paginate_related_orphans)
#         page_number = self.request.GET.get('page', 1)
#         page = paginator.get_page(page_number)
#         kwargs['page_obj'] = page
#         kwargs['articles'] = page.object_list
#         kwargs['is_paginated'] = page.has_other_pages()
#         return super().get_context_data(**kwargs)


# class UserChangeView(UpdateView):
#     model = get_user_model()
#     form_class = UserChangeForm
#     template_name = 'user_change.html'
#     context_object_name = 'user_obj'
#     def get_context_data(self, **kwargs):
#         if 'profile_form' not in kwargs:
#             kwargs['profile_form'] = self.get_profile_form()
#         return super().get_context_data(**kwargs)
#     def post(self, request, *args, **kwargs):
#         self.object = self.get_object()
#         form = self.get_form()
#         profile_form = self.get_profile_form()
#         if form.is_valid() and profile_form.is_valid():
#             return self.form_valid(form, profile_form)
#         else:
#             return self.form_invalid(form, profile_form)
#     def form_valid(self, form, profile_form):
#         response = super().form_valid(form)
#         profile_form.save()
#         return response
#     def form_invalid(self, form, profile_form):
#         context = self.get_context_data(form=form, profile_form=profile_form)
#         return self.render_to_response(context)
#     def get_profile_form(self):
#         form_kwargs = {'instance': self.object.profile}
#         if self.request.method == 'POST':
#             form_kwargs['data'] = self.request.POST
#             form_kwargs['files'] = self.request.FILES
#         return ProfileChangeForm(**form_kwargs
#     def get_success_url(self):
#         return reverse('accounts:detail', kwargs={'pk': self.object.pk})
