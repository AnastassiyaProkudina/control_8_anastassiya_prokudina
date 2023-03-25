from django.db.models import Manager, Sum, F, Avg


class ReviewManager(Manager):
    def get_avg(self, product_id):
        avg_grade = (
            self.get_queryset().filter(grade__gt=0).aggregate(Avg("grade"))
        )
        return avg_grade["qty__avg"]


