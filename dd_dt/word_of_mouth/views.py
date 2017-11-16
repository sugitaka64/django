from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.core.paginator import Paginator
from django.core.paginator import EmptyPage
from django.core.paginator import PageNotAnInteger
from .models import Comment
from .models import AnalyzeSentiment

def index(request):
    latest_lists = AnalyzeSentiment\
        .objects\
        .select_related('comment')\
        .values(
            'comment__id',
            'comment__comment',
            'comment__raiting',
            'comment__post_date',
            'score',
            'magnitude'
        )\
        .order_by('score')
    context = {
        'latest_lists': latest_lists,
    }
    return render(request, 'word_of_mouth/index.html', context)

def detail(request, word_of_mouth_id):
    comment = get_object_or_404(Comment, pk=word_of_mouth_id)
    context = {
        'comment': comment,
    }
    return render(request, 'word_of_mouth/detail.html', context)
