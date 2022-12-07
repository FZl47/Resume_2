from django.core.cache import cache

class CacheMixin:

    def save(self,*args,**kwargs):
        super(CacheMixin,self).save(*args,**kwargs)
        cache.clear()

    def delete(self,*args,**kwargs):
        super(CacheMixin,self).delete(*args,**kwargs)
        cache.clear()


