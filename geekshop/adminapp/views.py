from authapp.models import ShopUser
from mainapp.models import ProductCategory
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from .forms import ShopUserAdminEditForm, ShopUserAdminRegisterForm, ProductCategoryAdminForm


class UsersListView(ListView):
    model = ShopUser
    template_name = 'adminapp/list.html'
    queryset = ShopUser.objects.all()

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(UsersListView, self).get_context_data(**kwargs)
        context['title'] = 'Пользователи'
        context['create_tag'] = 'Добавить нового пользователя'
        context['create_link'] = 'admin_custom:user_create'
        context['update_link'] = 'admin_custom:user_update'
        context['users'] = ShopUser.objects.all()
        return context


class UserUpdateView(UpdateView):
    model = ShopUser
    template_name = 'adminapp/object_update.html'
    success_url = reverse_lazy('admin_custom:users')
    form_class = ShopUserAdminEditForm

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(UserUpdateView, self).get_context_data(**kwargs)
        title = ShopUser.objects.get(pk=self.kwargs.get('pk')).username
        context['title'] = 'Изменение пользователя: {}'.format(title)
        context['tag'] = 'Удалить пользователя'
        context['delete_link'] = 'admin_custom:user_delete'
        return context


class UserCreateView(CreateView):
    model = ShopUser
    template_name = 'adminapp/object_update.html'
    success_url = reverse_lazy('admin_custom:users')
    form_class = ShopUserAdminRegisterForm

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(UserCreateView, self).get_context_data(**kwargs)
        context['title'] = 'Создание нового пользователя. Админка'
        context['tag'] = 'Удалить категорию'
        return context


class UserDeleteView(DeleteView):
    model = ShopUser
    template_name = 'adminapp/object_delete.html'
    success_url = reverse_lazy('admin_custom:users')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(UserDeleteView, self).get_context_data(**kwargs)
        title = ShopUser.objects.get(pk=self.kwargs.get('pk')).username
        context['title'] = 'Удаление {}. Админка'.format(title)
        return context


class ProductCategoriesListView(ListView):
    model = ProductCategory
    template_name = 'adminapp/list.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ProductCategoriesListView, self).get_context_data(**kwargs)
        context['title'] = 'Категории'
        context['create_tag'] = 'Создать новую категорию'
        context['create_link'] = 'admin_custom:category_create'
        context['update_link'] = 'admin_custom:category_update'
        context['categories'] = ProductCategory.objects.all()
        return context


class ProductCategoryUpdateView(UpdateView):
    model = ProductCategory
    template_name = 'adminapp/object_update.html'
    success_url = reverse_lazy('admin_custom:categories')
    form_class = ProductCategoryAdminForm

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ProductCategoryUpdateView, self).get_context_data(**kwargs)
        title = ProductCategory.objects.get(pk=self.kwargs.get('pk')).name
        context['title'] = 'Изменение категории: {}'.format(title)
        context['tag'] = 'Удалить категорию'
        context['delete_link'] = 'admin_custom:category_delete'
        return context


class ProductCategoryDeleteView(DeleteView):
    model = ProductCategory
    template_name = 'adminapp/object_delete.html'
    success_url = reverse_lazy('admin_custom:categories')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ProductCategoryDeleteView, self).get_context_data(**kwargs)
        title = ProductCategory.objects.get(pk=self.kwargs.get('pk')).name
        context['title'] = 'Удаление {}'.format(title)
        return context


class ProductCategoryCreateView(CreateView):
    model = ProductCategory
    template_name = 'adminapp/object_update.html'
    success_url = reverse_lazy('admin_custom:categories')
    form_class = ProductCategoryAdminForm

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ProductCategoryCreateView, self).get_context_data(**kwargs)
        context['title'] = 'Создание новой категории.'
        context['tag'] = 'Удалить категорию'
        return context

