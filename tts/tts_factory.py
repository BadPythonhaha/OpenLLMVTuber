from typing import Type
from .tts_interface import TTSInterface


class TTSFactory:
    @staticmethod
    def get_tts_engine(engine_type: str = 'meloTTS', **kwargs) -> Type[TTSInterface]:
        if engine_type == "meloTTS":
            from .meloTTS import TTSEngine as MeloTTSEngine

            return MeloTTSEngine(
                speaker=kwargs.get("speaker"),
                language=kwargs.get("language"),
                device=kwargs.get("device"),
                speed=kwargs.get("speed"),
            )
        else:
            raise ValueError(f"Currently, only meloTTS is supported. Received: {engine_type}")


# Example usage:
# tts_engine = TTSFactory.get_tts_engine("azure", api_key="your_api_key", region="your_region", voice="your_voice")
# tts_engine.speak("Hello world")
