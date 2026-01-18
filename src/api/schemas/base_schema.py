from pydantic import BaseModel, ConfigDict


class BaseSchema(BaseModel):
    model_config = ConfigDict(
        extra="forbid",          # Запрещаем неожиданные поля
        from_attributes=True,    # Позволяет работать с объектами (если надо) (аналог orm_mode)
        validate_assignment = True  # защита от кривых изменений
    )