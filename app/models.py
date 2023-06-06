from django.db.models import *
from django.conf import settings

class Books(Model):
	name = CharField(max_length=60, verbose_name='Название')
	image = ImageField(verbose_name='Фото')
	description = TextField(max_length=300, 
		verbose_name='Дополнительная информация')
	price = DecimalField(max_digits=10, decimal_places=2, 
		verbose_name='Стоимость')
	author = ForeignKey(settings.AUTH_USER_MODEL, on_delete=CASCADE)
	pub_date = DateField(auto_now_add=True)

	def __str__(self):
		return f'{self.name} | {self.price}'