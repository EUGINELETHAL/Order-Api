from django.shortcuts import render

# Create your views here.
class TodoListCreateAPIView(ListCreateAPIView):
    serializer_class = TodoSerializer

    def get_queryset(self):
        return Todo.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        class InvoiceViewSet(ModelViewSet):
    queryset = Invoice.objects.all()
    serializer_class = InvoiceSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user, status=Invoice.SENT)serializer.save(user=self.request.user)

class SubjectList(APIView):
    def get(self, request, format=None):
        all_subjects = Subject.objects.all()
        serializers = SubjectSerializer(all_subjects, many=True)
        return Response(serializers.data)

    def post(self, request, format=None):
        serializers = SubjectSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

