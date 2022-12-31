from django.contrib import admin
from rules.models import Rule, Result

# Register your models here.

admin.site.register(Rule)


@admin.register(Result)
class ResualtAdmin(admin.ModelAdmin):

    filter_horizontal = ("rule_function",)
    list_display = ("resualt_name", "validation")
    readonly_fields = ["validation"]

    def validation(self, obj):
        func = {}
        rules = obj.rule_function.all()
        for item in rules:
            try:
                res = eval(item.rule_function)
            except Exception as e:
                res = e
            print(res)
            func[item.rule_name] = str(res)
        return func
