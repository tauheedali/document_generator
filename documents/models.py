from django.db import models


# Create your models here.
class BaseModel(models.Model):
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Template(BaseModel):
    title = models.CharField(max_length=255)
    template_file = models.FileField(upload_to='uploads/documents/templates', unique=True)
    doc_type = models.CharField(max_length=100, blank=True, null=True)
    notes = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title


class Document(BaseModel):
    name = models.CharField(max_length=255)
    file = models.FileField(upload_to='uploads/documents', blank=True, null=True, unique=True)
    template = models.ForeignKey(Template, on_delete=models.DO_NOTHING, blank=True, null=True)


class FieldType(BaseModel):
    field_type = models.CharField(max_length=100)
    internal_field = models.BooleanField(default=False)


class Field(BaseModel):
    field = models.CharField(max_length=100)
    value = models.TextField()
    field_type = models.ForeignKey(FieldType, on_delete=models.DO_NOTHING)
    template = models.ForeignKey(Template, on_delete=models.DO_NOTHING)
