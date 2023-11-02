from django.urls import path
from django_rest_passwordreset.views import reset_password_request_token, reset_password_confirm
import program.shop.views

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('product', program.ProductViewSet)
router.register('shops', program.ShopViewSet)
router.register('categories', program.CategoryView)

app_name = 'shop'

urlpatterns = [
                  path('user/register', program.RegisterAccount.as_view()),
                  path('user/register/confirm', program.ConfirmAccount.as_view()),
                  path('user/login', program.LoginAccount.as_view()),
                  path('user/details', program.AccountDetails.as_view()),

                  path('products', program.ProductInfoView.as_view()),

                  path('basket', program.BasketView.as_view()),

                  path('partner/update', program.PartnerUpdate.as_view()),
                  path('partner/state', program.PartnerState.as_view()),
                  path('partner/orders', program.PartnerOrders.as_view()),
                  path('partner/nameurl', program.PartnerNameUrl.as_view()),

                  path('user/contact', program.ContactView.as_view(), name='user-contact'),
                  path('user/password_reset', reset_password_request_token, name='password-reset'),
                  path('user/password_reset/confirm', reset_password_confirm, name='password-reset-confirm'),

                  path('order', program.OrderView.as_view(), name='order'),

              ] + router.urls
