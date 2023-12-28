import os
import sys
import urllib
import urllib.request
import json
import time
from .... import errors

gameName: str = "maplestorym"


class mapleMapi:
    headers: dict = {"accept": "application/json", }
    validWorld: list = ['아케인', '크로아', '엘리시움', '루나', '스카니아', '유니온', '제니스']
    globalUrl: str = f"https://open.api.nexon.com/{gameName}/v1/"

    def __init__(this, key: str) -> None:
        this.headers["x-nxopen-api-key"] = key

    def validifyWorldStr(this, world: str) -> bool:
        if world in this.validWorld:
            return True
        return False

    # get ocid
    def getOcid(this, name: str, world: str) -> str:
        f'''
        MapleStoryM 캐릭터 닉네임으로부터 OCID를 가져옵니다.

        name: str: 캐릭터 닉네임
        world: str: 월드명 (다음 중 하나: {this.validWorld})

        InvalidWorldError: 월드 명이 유효하지 않을 때 발생합니다. open.api.nexon.com::OPENAPI00004를 대체할 때 사용됩니다.
        '''

        if not this.validifyWorldStr(world):
            raise errors.InvalidWorldError(
                world, this.validWorld
            )

        _url: str = f"{this.globalUrl}id?character_name={name}&world_name={world}"
        request: urllib.request.Request = urllib.request.Request(
            _url, headers=this.headers)
        try:
            response = urllib.request.urlopen(request)
            _code = response.getcode()
        except Exception as e:
            if _code == 429:
                raise errors.TooManyRequestsError()

            print(response)
            print(e)
            return ""

        ocid: str = json.loads(response.read())['ocid']

        return ocid
