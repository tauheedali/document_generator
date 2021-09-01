from django.contrib.auth.models import User
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from mailmerge import MailMerge
from .models import Document

print('ready imported')


def get_field(mod, name):
    components = name.split('.')
    # mod = __import__(components[0])
    for comp in components[1:]:
        mod = getattr(mod, comp)
        if callable(mod):
            mod = mod()
    return mod


@receiver(pre_save, sender=Document)
def save_document(sender, instance, **kwargs):
    if instance.template is not None:
        doc_template = instance.template.template_file
        doc_template = MailMerge(doc_template)
        fields = {}

        class Test:
            def test(self):
                return '12345'

        for field in instance.template.field_set.all():
            if field.field_type.internal_field:
                fields[field.field] = get_field(Test(), field.value)
            else:
                fields[field.field] = field.value

        doc_template.merge(**fields)
        path = "uploads/documents/{}.docx".format(instance.name)
        doc_template.write(path)
        instance.file = path
        # print(doc_template.get_merge_fields())

    else:
        print('File already exists')
    print(dict(kwargs))
