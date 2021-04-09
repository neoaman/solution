# Importing Buildin INTERNAL Modules
from bson import ObjectId
import json

# Importing the EXTRENAL MODULES
from rest_framework.views import APIView,Response,status
# Authentication Functions
from rest_framework.authentication import TokenAuthentication,SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated, BasePermission, SAFE_METHODS,IsAuthenticatedOrReadOnly

# importing LOCAL MODULES
from .models import BlogPost
from .serializers import BlogPostSerializer
# Importing utility functions/class
from toolkit.mongotools import mongodb
from toolkit.templatetags.template_extra import md_safe


class NeoAUTH(TokenAuthentication):
    keyword = 'neoauth'

class ReadOnly(BasePermission):
    def has_permission(self, request, view):
        return request.method in SAFE_METHODS
        # return request.method in ['GET','POST']


# Class and function for API view
class BlogPostView(APIView):
    """
    Blog Post with Auto generated <span style="color:'red'">ID</span>
    """
    name = "Blog API"

    serializer_class = BlogPostSerializer
    collection = mongodb(use="blog")
    lookup_field = "postId"
    json_fields = BlogPost.json_field
    authentication_classes = [SessionAuthentication,NeoAUTH]
    # authentication_classes = [NeoAUTH]
    # permission_classes = [IsAuthenticated|ReadOnly]
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get(self, request, pk=None, format=None):
        # try:
        #     context = [self.serializer_class(i).data for i in self.collection.filter({})]
        # except:
        #     context = [{"error":"No data Found"},{"info":"Add some data"}]
        context = [self.serializer_class(i,context={'request':request}).data for i in self.collection.filter({})]

        return Response(context,status=status.HTTP_200_OK)
    
    def post(self, request, format=None):

        data = self.serializer_class(request.data).data

        for i in self.json_fields : data[i] = json.loads(data[i])
        self.collection.add(value=data)
        return Response(self.serializer_class(data,context={'request':request}).data, status=status.HTTP_200_OK)

class BlogIndividualPostView(APIView):
    """
    Blog Post with Auto generated __ID__
    """
    name = "Blog Instance View"

    serializer_class = BlogPostSerializer
    collection = mongodb(use="blog")
    lookup_field = "postId"
    json_fields = BlogPost.json_field

    # authentication_classes = [SessionAuthentication, BasicAuthentication,TokenAuthentication]
    authentication_classes = [SessionAuthentication,NeoAUTH]
    permission_classes = [IsAuthenticated]

    
    def get(self, request, pk=None,**kwargs):
        print(request.user)
        context = self.serializer_class(self.collection.get({self.lookup_field:pk}),context={'request':request}).data
                
        return Response(context, status=status.HTTP_200_OK)
    
    def put(self, request, pk=None,**kwargs):
        
        data = self.serializer_class(request.data).data
        # print(data)
        for i in self.json_fields: data[i] = json.loads(data[i])
        self.collection.set_all({self.lookup_field:pk},data)

        context = self.serializer_class(self.collection.get({self.lookup_field:pk}),context={'request':request}).data
        # return Response(context, status=status.HTTP_200_OK)

        return Response(context, status=status.HTTP_200_OK)

    def patch(self, request, pk=None,**kwargs):
        data = self.serializer_class(request.data).data
        for i in self.json_fields: data[i] = json.loads(data[i])
        self.collection.set_all({self.lookup_field:pk},data)

        context = self.serializer_class(self.collection.get({self.lookup_field:pk}),context={'request':request}).data
        return Response(context, status=status.HTTP_200_OK)
    
    def delete(self, request, pk=None,**kwargs):
        
        self.collection.delete({self.lookup_field:pk})
        context={"info":f"Object with ID {pk} Deleted sucessfully"}

        return Response(context, status=status.HTTP_200_OK)