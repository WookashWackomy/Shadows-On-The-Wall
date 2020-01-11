from django.http import HttpResponse

from revolution.models import Problem, Tag, Comment, AppUser, Entry, Initiative, Solution
from revolution.serializers import ProblemSerializer, NewProblemSerializer, TagSerializer,\
    CommentSerializer, AppUserDetailsSerializer, GraphSerializer

from rest_framework import generics, viewsets
from rest_framework.decorators import action
from django.shortcuts import get_object_or_404
from rest_framework.response import Response


class ProblemDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Problem.objects.all()
    serializer_class = NewProblemSerializer


class NewProblem(generics.CreateAPIView):
    queryset = Problem.objects.all()
    serializer_class = NewProblemSerializer


class AddCommentMixin:
    def add_comment(self, entry, content):
        serializer = CommentSerializer(data=content)
        if serializer.is_valid():
            comment = serializer.save()
            entry.add_comment(comment)


class AddCommentToProblem(generics.CreateAPIView, AddCommentMixin):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def post(self, request, *args, **kwargs):
        entry = get_object_or_404(Problem, pk=kwargs["pk"])
        self.add_comment(entry, request.data)
        return HttpResponse(status=200)


class AddCommentToInitiative(generics.CreateAPIView, AddCommentMixin):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def post(self, request, *args, **kwargs):
        entry = get_object_or_404(Initiative, pk=kwargs["pk"])
        self.add_comment(entry, request.data)
        return HttpResponse(status=200)


class AddCommentToSolution(generics.CreateAPIView, AddCommentMixin):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def post(self, request, *args, **kwargs):
        entry = get_object_or_404(Solution, pk=kwargs["pk"])
        self.add_comment(entry, request.data)
        return HttpResponse(status=200)


class TagList(generics.ListAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


class NewTag(generics.CreateAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


class CommentList(generics.ListAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class AppUserDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = AppUser.objects.all()
    serializer_class = AppUserDetailsSerializer


class GraphViewSet(viewsets.ViewSet):
    @action(detail=True, methods=['GET'])
    def retrieve_problem(self, request, pk):
        problem = get_object_or_404(Problem, pk=pk)
        serializer = GraphSerializer(problem.get_graph())
        return Response(serializer.data)

    @action(detail=True, methods=['GET'])
    def retrieve_initiative(self, request, pk):
        initiative = get_object_or_404(Initiative, pk=pk)
        serializer = GraphSerializer(initiative.get_graph())
        return Response(serializer.data)


problem_graph = GraphViewSet.as_view({'get': 'retrieve_problem'})
initiative_graph = GraphViewSet.as_view({'get': 'retrieve_initiative'})

