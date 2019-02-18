from django.contrib import admin
from .models import Post
from .models import Comment

# admin에서 모든 model을 넣을 필요는 없음. admin에서 관리하고싶은 것만 등록
# CRUD 중에 고를 수 있음
# admin.site.register(Post)
# admin.site.register(Comment) #기본 ModelAdmin 으로 동작

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    pass

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    pass