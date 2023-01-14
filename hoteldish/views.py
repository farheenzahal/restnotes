from rest_framework.views import APIView
from rest_framework.viewsets import ViewSet,ModelViewSet
from rest_framework.response import Response
from .models import Dish,Review
from .serializers import Dishserializer,DishmodelSerializer,Userserializer,Reviewserializer
from rest_framework import status,permissions,authentication
from rest_framework.decorators import action


class DishView(APIView):
    serializer_class=DishmodelSerializer
    def get(self,request,*args,**kargs):
        all_dishes=Dish.objects.all()
        serializer=self.serializer_class(all_dishes,many=True)
        return Response(data=serializer.data)
   
    def post(self,request,*args,**kargs):
        serializer=self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)

    
class Dishdetailsview(APIView):
    serializer_class=DishmodelSerializer
    def get(self,request,*args,**kargs):
        id=kargs.get("id")
        try:
            dish_detail=Dish.objects.get(id=id)
            serializer=self.serializer_class(dish_detail)
            return Response(data=serializer.data)
        except:
            return Response({"msg":"invalid"})
    
    
    def delete(self,request,*args,**kargs):
        id=kargs.get("id")
        try:
            dish_detail=Dish.objects.get(id=id)
            dish_detail.delete()
            serializer=self.serializer_class(dish_detail)
            return Response(data=serializer.data)
        except:
            return Response({"msg":"invalid"})
    
    def put(self,request,*args,**kargs):
        id=kargs.get("id")
        dishs=Dish.objects.get(id=id)
        serializer=self.serializer_class(data=request.data,instance=dishs)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)
        
class Signup(APIView):
    def post(self,request,*args,**kargs):
        serializer=Userserializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)


class NewDish(ViewSet):
    def list(self,request,*args,**kargs): 
        qs=Dish.objects.all()
        try:
            if "category" in request.query_params:
                category=request.query_params.get(("category"))
                qs=qs.filter(category=category)
            if "price_lt" in request.query_params:
                price_lt=request.query_params.get("price_lt")  
                qs=qs.filter(price_lte=price_lt) 
            print(1)
            serial=DishmodelSerializer(qs,many=True)
            return Response(data=serial.data)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)   

    def create(self,request,*args,**kargs):
        serial=DishmodelSerializer(data=request.data)
        if serial.is_valid():
            serial.save()
            return Response(data=serial.data)
        else:
            return Response(data=serial.errors) 

    def update(self,request,*args,**kargs):
        id=kargs.get("pk")
        dishs=Dish.objects.get(id=id)
        serial=DishmodelSerializer(data=request.data,instance=dishs)
        if serial.is_valid():
            serial.save()
            return Response(data=serial.data)
        else:
            return Response(data=serial.errors)

    def destroy(self,request,*args,**kargs):
        id=kargs.get("pk")
        try:
            dish_detail=Dish.objects.get(id=id)
            dish_detail.delete()
            serial=DishmodelSerializer(dish_detail)
            return Response(data=serial.data)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def retrieve(self,request,*args,**kargs): 
        id=kargs.get("pk")
        try:
            dish_detail=Dish.objects.get(id=id)
            serial=DishmodelSerializer(dish_detail)
            return Response(data=serial.data)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)


class Dishmodelviewset(ModelViewSet):
    # authentication_classes=[authentication.TokenAuthentication]
    permission_classes=[permissions.IsAuthenticated]
    serializer_class=DishmodelSerializer
    queryset=Dish.objects.all()
    model=Dish

    @action(detail=True,methods=["get"])
    def get_review(self,request,*args,**kargs):
        id=kargs.get("pk")
        dish=Dish.objects.get(id=id)
        review=Review.objects.filter(dish=dish)
        serail=Reviewserializer(review,many=True)
        if serail.is_valid():
            serail.save()
            return Response(data=serail.data)
        else:
            return Response(data=serail.errors)    

    


            
