from django.urls import include, path

from . import views
app_name = 'tractebel'
urlpatterns = [
    # WELCOME
    path('welcome/', views.welcome, name='welcome'),

    # BUSINESS LINE
    path('list/', views.BusinessLineListView.as_view(), name='businessline_list'),
    path('add/', views.BusinessLineCreateView.as_view(), name='business_add'),
    path('edit/<int:pk>/', views.BusinessLineUpdateView.as_view(), name='business_change'),
    path('delete/<int:pk>', views.BusinessLineDeleteView.as_view(), name='business_delete'),

    # PROFIT CENTER
    path('profit_list/', views.ProfitCenterListView.as_view(), name='profit_list'),
    path('profit_add/', views.ProfitCenterCreateView.as_view(), name='profit_add'),
    path('profit_edit/<int:pk>/', views.ProfitCenterUpdateView.as_view(), name='profit_change'),
    path('profit_delete/<int:pk>', views.ProfitCenterDeleteView.as_view(), name='profit_delete'),

    # PROJECT
    path('project_list/', views.ProjectListView.as_view(), name='project_list'),
    path('project_add/', views.ProjectCreateView.as_view(), name='project_add'),
    path('project_edit/<int:pk>/', views.ProjectUpdateView.as_view(), name='project_change'),
    path('project_delete/<int:pk>', views.ProjectDeleteView.as_view(), name='project_delete'),

    path('ajax/load-profits/', views.load_profit_center, name='ajax_load_profits'),


]
