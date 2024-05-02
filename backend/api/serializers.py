# Модуль сериализаторов API.
from rest_framework import serializers

from donations.models import Donation
from contacts.models import Contact
from forbiddenwords.models import ForbiddenWord
from mixplat.models import MixPlat


class DonationSerializer(serializers.ModelSerializer):
    """Сериализатор пожертвований."""

    class Meta:
        model = Donation
        fields = (
            "id",
            "email",
            "donat",
            "custom_donat",
            "payment_method",
            "monthly_donat",
            "subscription",
        )


class MixPlatSerializer(serializers.ModelSerializer):
    """Сериализатор платежа Mixplat."""

    class Meta:
        model = MixPlat
        fields = (
            "id",
            "email",
            "donat",
            "custom_donat",
            "payment_method",
            "monthly_donat",
            "subscription",
            "payment_id",
            "status",
            "user_account_id",
            "user_comment",
            "date_created",
            "date_processed",
        )


class ContactSerializer(serializers.ModelSerializer):
    """Сериализатор контактов."""

    class Meta:
        model = Contact
        fields = ("username", "email", "subject", "comment")


class ForbiddenwordSerializer(serializers.ModelSerializer):
    """Сериализатор запрещенных слов."""

    class Meta:
        model = ForbiddenWord
        fields = ("forbidden_word",)
