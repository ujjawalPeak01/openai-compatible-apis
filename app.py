import os
import json
from transformers import pipeline


class InferlessPythonModel:

    def initialize(self):
        self.generator = pipeline("text-generation", model="EleutherAI/gpt-neo-125M",device=0)
        print("This is Initialize Code", flush=True)

    
    def infer(self, inputs):
        prompt = inputs.get("text_input")
        min_length = inputs.get("min_length")
        max_new_tokens = inputs.get("max_new_tokens")
        pipeline_output = self.generator(prompt, do_sample=True, min_length=min_length, max_new_tokens=max_new_tokens)
        generated_txt = pipeline_output[0]["generated_text"]
        return {"generated_text": generated_txt}

    def finalize(self,args):
        self.pipe = None
