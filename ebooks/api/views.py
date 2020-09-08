from rest_framework import generics,mixins
from ebooks.models import Ebook,Review
from ebooks.api.serializers import EbookSerializer,ReviewSerializer
from rest_framework.generics import get_object_or_404 
from rest_framework import permissions

from ebooks.api.pagination import SmallSetPagination


class EbookListCreateAPIView(generics.ListCreateAPIView):
    queryset = Ebook.objects.all().order_by("-id")
    serializer_class = EbookSerializer
    pagination_class = SmallSetPagination
    # permission_classes= [permissions.IsAuthenticatedOrReadOnly]

class EbookDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Ebook.objects.all()
    serializer_class = EbookSerializer
    

class ReviewCreateAPIView(generics.CreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer    
    
    def perform_create(self, serializer):
        ebook_pk = self.kwargs.get("ebook_pk")
        ebook = get_object_or_404(Ebook,pk=ebook_pk)
        serializer.save(ebook=ebook)
    
    
class ReviewDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
     queryset = Review.objects.all()
     serializer_class = ReviewSerializer
    
# class EbookListCreateAPIView(mixins.ListModelMixin,
#                              mixins.CreateModelMixin,
#                              generics.GenericAPIView):

#     queryset= Ebook.objects.all()
#     serializer_class= EbookSerializer
    
#     def get(self,request,*args,**kwargs):
#         return self.list(request,*args,**kwargs)
    
#     def post(self,request,*args,**kwargs):
#         return self.create(request,*args,**kwargs)


