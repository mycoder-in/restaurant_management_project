from rest_frameworks import serializers
from .models import Coupon

class CouponSerializer(serializer.ModelSerializer):
    class Meta:
        model = Coupon
        fields = ['code','discount_percentage','is_active','valid_form','valid_until']