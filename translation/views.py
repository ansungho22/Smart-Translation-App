from rest_framework.response import Response
from rest_framework.views import APIView
import os
from google.cloud import translate_v2 as translate

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = r"/Code/chatroom/chatty/smarth-322600-e26f149eb53f.json"
translate_client = translate.Client()


class GoogleTranslationAPIView(APIView):
    def post(self, request):
        contents = request.data["contents"]
        language = request.data["language"]
        result = translate_client.translate(contents, target_language=language)
        return Response(result["translatedText"], status=201)
