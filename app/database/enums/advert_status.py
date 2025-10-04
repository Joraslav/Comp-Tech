from enum import StrEnum


class AdvertStatus(StrEnum):
    DRAFT = "draft"
    PUBLISHED = "published"
    ARCHIVED = "archived"
    MODERATION = "moderation"
