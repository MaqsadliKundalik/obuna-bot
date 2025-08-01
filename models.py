from tortoise import models, fields

class User(models.Model):
    id = fields.BigIntField(pk=True)
    telegram_id = fields.BigIntField(unique=True)
    name = fields.CharField(max_length=255)
    status = fields.CharField(max_length=50, default="active")
    updated_at = fields.DatetimeField(auto_now=True)
    created_at = fields.DatetimeField(auto_now_add=True)

    class Meta:
        table = "users"

    def __str__(self):
        return f"{self.name} ({self.id})"