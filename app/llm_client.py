from typing import List, Tuple, AsyncIterator


class BaseLLMClient:
    async def generate(self, prompt: str, history: List[Tuple[str,str]]) -> Tuple[str, List[Tuple[str,str]]]:
        raise NotImplementedError
    async def astream(self, prompt: str, history: List[Tuple[str,str]]) -> AsyncIterator[str]:
        raise NotImplementedError



