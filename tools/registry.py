import json
import requests
from langchain_core.tools import tool
from sqlmodel import Enum
import os
from shared.utils import get_skill_description
from tools.mcp.somtihng import something_tool

def get_select_skills_prompt(path: str) -> str:
    all_prompts = []
    skill_path = os.path.join(path, "SKILL.md")
    if os.path.exists(skill_path):
        description = get_skill_description(skill_path)
        all_prompts.append(description)
    return "\n\n".join(all_prompts)

# class enum
class something(str,   Enum):
    something = "something"

@tool("something", return_direct=True)
def something(something: str,number: str) -> str:
    """
    function for getting the skills from the registry
    """
    try:
        return something_tool(something, number)
    except Exception as e:
        return f"Error getting skills: {e}"