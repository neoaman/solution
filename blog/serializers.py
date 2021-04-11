# EXTERNAL APPS
from rest_framework import serializers
from rest_framework.reverse import reverse

# LOCAL APPS
from .models import BlogPost
from toolkit.mongotools import Mongodb


def auto_id():
    lookup_field = "postId"
    collection = Mongodb("blog")
    latest_data = collection.get({},sort=[('_id',-1)])
    if not latest_data: latest_data={}
    id_ = str(int(latest_data.get(lookup_field,0))+1)
    return id_

class BlogPostSerializer(serializers.ModelSerializer):
    url = serializers.SerializerMethodField()
    content = serializers.CharField(
        # max_length=1000,
        style={'base_template': 'textarea.html', 'rows': 30})
    image = serializers.CharField()
    class Meta:
        model = BlogPost
        fields = ("postId","title","tag","image","subTitle","content","publishDate","draft","url")

        extra_kwargs = {'draft': {'default': False},
        'postId':{'initial':auto_id},
        }
    
    def get_url(self,obj):
        # print(obj.get("postId")); print(self.context['request'])
        try: url = reverse("api:blog_instance",kwargs={'pk': obj.get("postId")},request=self.context.get('request',None))
        except: print("Can't get the instance url"); url = ""
        return url