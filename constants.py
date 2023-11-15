import streamlit as st
from utils.constants import *
import torch
from llama_index import (GPTVectorStoreIndex, SimpleDirectoryReader, LLMPredictor, 
                         ServiceContext, LangchainEmbedding)
from langchain.embeddings import HuggingFaceInstructEmbeddings
from ibm_watson_machine_learning.foundation_models.extensions.langchain import WatsonxLLM
from ibm_watson_machine_learning.foundation_models.utils.enums import ModelTypes, DecodingMethods
from ibm_watson_machine_learning.metanames import GenTextParamsMetaNames as GenParams
from ibm_watson_machine_learning.foundation_models import Model