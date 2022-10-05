import random
import string
from django.test import TestCase
from Blog.models import Blog


class BlogTestCase(TestCase):

        def test_creacion_blog(self):

                lista_letras_titulo = [random.choice(string.ascii_letters + string.digits) for _ in range(20)]
            
                lista_letras_subtitulo = [random.choice(string.ascii_letters + string.digits) for _ in range(30)]
            
                lista_letras_cuerpo = [random.choice(string.ascii_letters + string.digits) for _ in range(30)]
            
                titulo_prueba = "".join(lista_letras_titulo)
            
                subtitulo_prueba = "".join(lista_letras_subtitulo)
            
                cuerpo_prueba = "".join(lista_letras_cuerpo)
            
                blog_1 = Blog.objects.create(titulo=titulo_prueba,subtitulo=subtitulo_prueba,cuerpo=cuerpo_prueba)

                self.assertIsNotNone(blog_1.id)
            
                self.assertEqual(blog_1.titulo, titulo_prueba)
            
                self.assertEqual(blog_1.subtitulo, subtitulo_prueba)
            
                self.assertEqual(blog_1.cuerpo, cuerpo_prueba)
