from django.contrib.auth.mixins import UserPassesTestMixin
from authapp.models import ShopUser
from mainapp.models import ProductCategory, Product
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import DetailView
from django.views.generic.list import ListView
from .forms import ShopUserAdminEditForm, ShopUserAdminRegisterForm, ProductCategoryAdminForm, ProductAdminForm


class IsSuperUserView(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.is_superuser


class UsersListView(IsSuperUserView, ListView):
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


class UserUpdateView(IsSuperUserView, UpdateView):
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


class UserCreateView(IsSuperUserView, CreateView):
    model = ShopUser
    template_name = 'adminapp/object_update.html'
    success_url = reverse_lazy('admin_custom:users')
    form_class = ShopUserAdminRegisterForm

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(UserCreateView, self).get_context_data(**kwargs)
        context['title'] = 'Создание нового пользователя. Админка'
        context['tag'] = 'Удалить категорию'
        return context


class UserDeleteView(IsSuperUserView, DeleteView):
    model = ShopUser
    template_name = 'adminapp/object_delete.html'
    success_url = reverse_lazy('admin_custom:users')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(UserDeleteView, self).get_context_data(**kwargs)
        title = ShopUser.objects.get(pk=self.kwargs.get('pk')).username
        context['title'] = 'Удаление {}. Админка'.format(title)
        return context


class ProductCategoriesListView(IsSuperUserView, ListView):
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


class ProductCategoryUpdateView(IsSuperUserView, UpdateView):
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


class ProductCategoryDeleteView(IsSuperUserView, DeleteView):
    model = ProductCategory
    template_name = 'adminapp/object_delete.html'
    success_url = reverse_lazy('admin_custom:categories')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ProductCategoryDeleteView, self).get_context_data(**kwargs)
        title = ProductCategory.objects.get(pk=self.kwargs.get('pk')).name
        context['title'] = 'Удаление {}'.format(title)
        return context


class ProductCategoryCreateView(IsSuperUserView, CreateView):
    model = ProductCategory
    template_name = 'adminapp/object_update.html'
    success_url = reverse_lazy('admin_custom:categories')
    form_class = ProductCategoryAdminForm

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ProductCategoryCreateView, self).get_context_data(**kwargs)
        context['title'] = 'Создание новой категории.'
        context['tag'] = 'Удалить категорию'
        return context


class ProductListView(IsSuperUserView, ListView):
    model = Product
    template_name = 'adminapp/products.html'
    queryset = Product.objects.all()

    def get_queryset(self):
        queryset = super(ProductListView, self).get_queryset()
        if self.kwargs.get('category_pk'):
            queryset = queryset.filter(category=self.kwargs.get('category_pk'))
        return queryset

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ProductListView, self).get_context_data(**kwargs)
        context['title'] = 'Все продукты. Админка'
        context['categories'] = ProductCategory.objects.all()
        return context


class ProductDetailView(IsSuperUserView, DetailView):
    model = Product
    template_name = 'adminapp/product.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ProductDetailView, self).get_context_data(**kwargs)
        title = Product.objects.get(pk=self.kwargs.get('pk')).name
        context['title'] = '{}. Админка'.format(title)
        return context


class ProductCreateView(IsSuperUserView, CreateView):
    model = Product
    template_name = 'adminapp/product_update.html'
    success_url = reverse_lazy('admin_custom:products')
    fields = '__all__'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ProductCreateView, self).get_context_data(**kwargs)
        context['title'] = 'Создание нового продукта. Админка'
        return context


class ProductDeleteView(IsSuperUserView, DeleteView):
    model = Product
    template_name = 'adminapp/object_delete.html'
    success_url = reverse_lazy('admin_custom:products')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ProductDeleteView, self).get_context_data(**kwargs)
        title = Product.objects.get(pk=self.kwargs.get('pk')).name
        context['title'] = 'Удаление {}. Админка'.format(title)
        return context


class ProductUpdateView(IsSuperUserView, UpdateView):
    model = Product
    template_name = 'adminapp/product_update.html'
    success_url = reverse_lazy('admin_custom:products')
    form_class = ProductAdminForm

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ProductUpdateView, self).get_context_data(**kwargs)
        title = Product.objects.get(pk=self.kwargs.get('pk')).name
        context['title'] = 'Изменение {}. Админка'.format(title)
        return context

    def get_success_url(self):
        return reverse_lazy('admin_custom:product_read', kwargs={'pk': self.kwargs.get('pk')})