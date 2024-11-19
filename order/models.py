from django.db import models
from mysite.utils.base import BaseModel
from .forms import ContactForm

# Create your models here.



class Author(BaseModel):
    title = models.CharField(max_length= 150 , verbose_name= 'Title of the  author' , help_text= ' Maximum of 150 characters')



    class Meta :
        verbose_name = 'Author'
        verbose_name_plural = 'Authors'



    def __str__(self):
        return self.title
    


class Description(BaseModel):
    about= models.TextField(verbose_name='About of blog', help_text='Max 1000 characters' , blank=True , null=True)



    class Meta:
        verbose_name = 'Description'
        verbose_name_plural = 'All Description'

    def __str__(self):
        return self.about
    

class Tags (BaseModel):
    title= models.CharField(max_length= 100 , verbose_name='Title of the blog ' , help_text='Max 100 characters')
    

    class Meta:
        verbose_name = 'Tag'
        verbose_name_plural = 'All Tags'

    def __str__(self):
        return self.title



    
 


class Order (BaseModel):
    ORDER_TYPES  = (
        (0, 'Choose'),
        (1, 'Tech'),
        (2, 'Food'),
        (3, 'Travel'),
        (4, 'Lifestyle'),
    )
    title = models.CharField(max_length = 150 , verbose_name = 'Title of the order' , help_text = 'Maximum of 150 charcters')
    content = models.TextField(verbose_name= 'Content of the order')
    
    order_types = models.IntegerField(choices= ORDER_TYPES , default= 0 ,verbose_name= 'Type of the order')
    author= models.ForeignKey(Author, on_delete= models.CASCADE, verbose_name='Author of the order' , related_name='orderauthor')
    is_check = models.BooleanField(default= False, verbose_name= 'Check if the order is published')
    tags = models.ManyToManyField(Tags ,  verbose_name='Tags of the order' ,related_name='ordertags')
    cover_image = models.ImageField(upload_to= 'order/' , verbose_name= 'Cover Image of the  order ' ,help_text='Upload a cover image for the order' , blank= True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


    class Meta:
        verbose_name = 'Order'
        verbose_name_plural = "Order"
 


    def __str__(self):

      return self.title     



