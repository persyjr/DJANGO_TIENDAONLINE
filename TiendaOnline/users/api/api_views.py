from rest_framework.response import Response
from rest_framework.views   import APIView
from rest_framework.decorators import api_view
from users.models import User
from users.api.serializer import UserSerializer

##METODO GET ALL Y POST CON CLASE
class UserAPIView(APIView):
    def get(self, request):
        user = User.objects.all()
        users_serializer = UserSerializer(user, many=True)
        print(f'class UserAPIView {users_serializer}')
        return Response({"data":users_serializer.data})
    
    def post(self, request):
        print(request.data)
        users_serializer=UserSerializer(data= request.data)
        if users_serializer.is_valid(): #me permite validar mis datos ingresados, mejor que el forms
            users_serializer.save() #ME GUARDA EN EL MODELO USUARIOS LA INFO
            return Response({'res':'ok','data':users_serializer.data})
        return Response(users_serializer.errors)

class UserDetailAPIView(APIView):
    #vs¿ista de detalle para una perona nada mas
    def get(self, request,pk=None):
        user = User.objects.filter(id=pk).first()
        user_serializer=UserSerializer(user)
        return Response({'res':f'GET <{pk}>','data':user_serializer.data})
    
    def put(self, request,pk=None):
        user = User.objects.filter(id=pk).first()
        user_serializer=UserSerializer(user,data=request.data)#ME ACTUALIZA LA DATA CON EL REQUEST
        if user_serializer.is_valid():
            user_serializer.save() #ME GUARDA EN EL MODELO USUARIOS LA INFO
            return Response({'res':'PUT','data':user_serializer.data})
        return Response(user_serializer.errors)
        
    def delete(self, request,pk=None):
        user = User.objects.filter(id=pk).first()
        user.delete()
        return Response({'res':'DELETE','data':'USER_ELIMINADO'})



##METODO GET ALL Y POST CON FUNCION Y DECORADORES    
@api_view(['GET','POST'])
def user_api_view(request):
    if request.method == 'GET':
        queryset = User.objects.all()
        users_serializer = UserSerializer(queryset, many=True)
        print(f'function user_api_view  GET {users_serializer.data}\n')
        return Response({'data':users_serializer.data})
    
    if request.method == 'POST':
        users_serializer=UserSerializer(data= request.data)
        print(f'function user_api_view  POST {users_serializer}\n')
        if users_serializer.is_valid(): #me permite validar mis datos ingresados, mejor que el forms
            users_serializer.save() #ME GUARDA EN EL MODELO USUARIOS LA INFO
            return Response(users_serializer.data)
        
        return Response(users_serializer.errors)

@api_view(['GET','PUT','DELETE'])
def user_detail_api_view(request,pk=None):
    #vista de detalle para una perona nada mas
    if request.method=='GET':
        user = User.objects.filter(id=pk).first()
        user_serializer=UserSerializer(user)
        return Response({'res':f'GET <{pk}>','data':user_serializer.data})
    
    elif request.method=='PUT':
        user = User.objects.filter(id=pk).first()
        user_serializer=UserSerializer(user,data=request.data)#ME ACTUALIZA LA DATA CON EL REQUEST
        if user_serializer.is_valid():
            user_serializer.save() #ME GUARDA EN EL MODELO USUARIOS LA INFO
            return Response({'res':'PUT','data':user_serializer.data})
        return Response(user_serializer.errors)
        
    elif request.method=='DELETE':
        user = User.objects.filter(id=pk).first()
        user_serializer=UserSerializer(user)
        user.delete()
        return Response({'res':'DELETE','data':pk})#devuelvo el numero del id para que sea filtrado 