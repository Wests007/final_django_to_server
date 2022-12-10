from django import forms

from .models import Post, Comment, Group


class PostForm(forms.ModelForm):
    group = forms.ModelChoiceField(
        queryset=Group.objects.filter(admins_only=False),
        label='Группа, к которой будет относиться пост',
        help_text='Выбирете группу'
    )

    class Meta:
        model = Post

        fields = ('text', 'group', 'image',)

        labels = {
            'text': 'Текст поста',
            'image': 'Изображение для поста'
        }

        help_texts = {
            'text': 'Введите текст поста (обязательное поле)',
            'image': 'Прикрепите изображение к посту'
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment

        fields = ('text',)

        labels = {
            'text': 'Текст комментария'
        }

        help_texts = {
            'text': 'Введите текст комментария'
        }
