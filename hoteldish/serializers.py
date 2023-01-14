from rest_framework import serializers
from hoteldish.models import Dish,Review
from django.contrib.auth.models import User
# serializers to convert query set into json format by using serializer package

class Dishserializer(serializers.Serializer):
    name=serializers.CharField()
    category=serializers.CharField()
    price=serializers.IntegerField()


class DishmodelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dish
        fields = "__all__"

    def validate(self, data):
        price=data.get("price")
        if price<0:
            raise serializers.ValidationError("invalid price")
        else:
            return data


class Userserializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=["username","email","password"]

    def create(self,validated_data):
        return User.objects.create_user(**validated_data)


class Reviewserializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=["rating","review"]       


    def create(self,validated_data):
        user=self.context.get("user")
        dish=self.context.get("dish")
        return Review.objects.create(dish=dish,user=user,**validated_data)    