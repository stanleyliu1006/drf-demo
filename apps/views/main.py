from datetime import datetime
from rest_framework.views import APIView
from rest_framework.response import Response
from . import Helpers

class Root(APIView):

    def get(self, request):
        build_envs = Helpers()._read_build_env()
        localBuild = "localhost"
        return Response({
            'ok': True,
            'status': 200,
            'name': 'reece-addressbook-api',
            'version': {
                'build_branch': build_envs.get('BUILD_GIT_BRANCH', localBuild),
                'build_commit': build_envs.get('BUILD_GIT_COMMIT', localBuild),
                'build_author': build_envs.get('BUILD_GIT_AUTHOR', localBuild),
                'build_author_name': build_envs.get('BUILD_GIT_AUTHOR_NAME', localBuild),
                'build_repository': build_envs.get('BUILD_GIT_REPO_LINK', localBuild),
                'build_date': datetime.fromtimestamp(int(build_envs['BUILD_CREATED'])).isoformat() if 'BUILD_CREATED' in build_envs else localBuild,
                'build_number': build_envs.get('BUILD_NUMBER', localBuild)
            },
            'tagline': 'Reece address booking api'
        })


class Healthz(APIView):
    def get(self, request):
        return Response({'ok': True})
