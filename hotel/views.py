from rest_framework.views import APIView
from rest_framework.response import Response
from.models import dish_items

# Create your views here.
class DishView(APIView):
    def get(self,request,*args,**kargs):
        return Response(data=dish_items)


    def post(self,request,*args,**kargs): 
        new_item=request.data
        dish_items.append(new_item)
        return Response(data=dish_items)   


class Dishdetails(APIView):
    def get(self,request,*args,**kargs):
        code=kargs.get("decode")
        dish=[item for item in dish_items if item["id"]==code].pop()    
        return Response(data=dish)    

    def put(self,request,*args,**kargs):
        code=kargs.get("decode")
        dish=[item for item in dish_items if item["id"]==code].pop()    
        data=request.data
        dish.update(data)
        return Response(data=dish_items)  


    def delete(self,request,*args,**kargs):
        code=kargs.get("decode")
        dish=[item for item in dish_items if item["id"]==code].pop()  
        dish_items.remove(dish)  
        return Response(data=dish_items)         
