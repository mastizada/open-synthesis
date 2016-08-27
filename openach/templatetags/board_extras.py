from django.template.defaulttags import register
from openach.models import Evaluation, Eval
import logging


logger = logging.getLogger(__name__)


@register.simple_tag
def get_detail(dictionary, evidence_id, hypothesis_id):
    """Returns the evaluation Eval for a given hypothesis and piece of evidence"""
    return dictionary.get((evidence_id, hypothesis_id))


@register.filter
def detail_name(value):
    if value:
        return next(e[1] for e in Evaluation.EVALUATION_OPTIONS if e[0] == value.value)
    else:
        return None


@register.filter
def detail_classname(value):
    mapping = {
        Eval.consistent: "eval-consistent",
        Eval.inconsistent: "eval-inconsistent",
        Eval.very_inconsistent: "eval-very-inconsistent",
        Eval.very_consistent: "eval-very-consistent",
        Eval.not_applicable: "eval-not-applicable",
        Eval.neutral: "eval-neutral"
    }
    return mapping.get(value)


@register.simple_tag
def get_source_tags(dictionary, source_id, tag_id):
    """Performs a dictionary lookup, returning None if the key is not in the dictionary"""
    return dictionary.get((source_id, tag_id))




