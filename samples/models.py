from django.db import models
# from knit_webnotes.patterns.models import Pattern
# from knit_webnotes.tools.models import Tool
# from knit_webnotes.webnotes.models import Webnote
# from knit_webnotes.yarns.models import Yarn
#
#
# class Sample(models.Model):
#     length = models.IntegerField(null=False)
#     width = models.IntegerField(null=False)
#     stitches = models.IntegerField(null=True)
#     rows = models.IntegerField(null=True)
#     webnote = models.ManyToManyField(Webnote)
#     pattern = models.ForeignKey(Pattern, verbose_name='Выберите узор', on_delete=models.CASCADE, default=0)
#     tool = models.ForeignKey(Tool, verbose_name='Выберите инструмент', on_delete=models.CASCADE, default=0)
#     yarn = models.ForeignKey(Yarn, verbose_name='Выберите пряжу', on_delete=models.CASCADE, default=0)
