import os
import re
from secret_key import api_key
from langchain_community.llms import together
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain, SequentialChain

os.environ["TOGETHER_API_KEY"] = api_key

llm = together.Together(model="deepseek-ai/DeepSeek-R1-Distill-Llama-70B", temperature=0.3)

def generate_restaurant_name_items(cuisine):
    if not cuisine:
        return None

    # Restaurant name prompt
    name_chain = LLMChain(
        llm=llm,
        prompt=PromptTemplate(
            input_variables=["cuisine"],
            template="Suggest a name for an {cuisine} restaurant. Only list the name, nothing else."
        ),
        output_key="restaurant_name"
    )

    # Menu items prompt
    food_item_chain = LLMChain(
        llm=llm,
        prompt=PromptTemplate(
            input_variables=["restaurant_name"],
            template=(
                "List exactly 5 authentic menu items for the restaurant called {restaurant_name}. "
                "Respond ONLY with the 5 items as a single comma-separated list, with NO explanations, NO numbers, and NO extra text. "
                "For example: Dish1, Dish2, Dish3, Dish4, Dish5"
            )
        ),
        output_key="menu_items"
    )

    # Get restaurant name
    restaurant_name_raw = name_chain.run({"cuisine": cuisine}).strip()
    first_name = next((line for line in restaurant_name_raw.split('\n')
                       if line and len(line.split()) <= 6 and line[0].isalpha()), None)
    if not first_name:
        first_name = next((line.strip() for line in restaurant_name_raw.split('\n') if line.strip()), "")

    # Get menu items
    menu_items_raw = food_item_chain.run({"restaurant_name": first_name})
    menu_items = next((line.strip() for line in menu_items_raw.split('\n')
                       if line.count(',') >= 4 and '.' not in line), None)
    if not menu_items:
        match = re.search(r'([A-Za-z\s\-]+,\s*[A-Za-z\s\-]+(?:,\s*[A-Za-z\s\-]+){4,})', menu_items_raw)
        menu_items = match.group(1).strip() if match else (menu_items_raw.strip().split('\n')[-1] if menu_items_raw.strip() else "")

    return {
        "restaurant_name": first_name,
        "menu_items": menu_items
    }

# def generate_restaurant_name_items(cuisine):
#     # Prompt to get a restaurant name
#     prompt_template_name = PromptTemplate(
#         input_variables=["cuisine"],
#         template="Suggest a name for an {cuisine} restaurant. Only list the name, nothing else."
#     )

#     name_chain = LLMChain(
#         llm=llm,
#         prompt=prompt_template_name,
#         output_key="restaurant_name"
#     )

# # Prompt to get menu items for the restaurant

#     prompt_template_item = PromptTemplate(
#         input_variables=["restaurant_name"],
#         template=(
#             "List exactly 5 authentic menu items for the restaurant called {restaurant_name}. "
#             "Respond ONLY with the 5 items as a single comma-separated list, with NO explanations, NO numbers, and NO extra text. "
#             "For example: Dish1, Dish2, Dish3, Dish4, Dish5"
#         )
#     )

#     food_item_chain = LLMChain(
#         llm=llm,
#         prompt=prompt_template_item,
#         output_key="menu_items"
#     )

# # Sequential chain to get restaurant name and menu items
#     chain = SequentialChain(
#         chains=[name_chain, food_item_chain],
#         input_variables=["cuisine"],
#         output_variables=["restaurant_name", "menu_items"]
#     )

# # Run the chain for a specific cuisine
#     response = chain({"cuisine": cuisine})

# # --- Extract the restaurant name ---
#     restaurant_name_raw = response["restaurant_name"]
#     first_name = None
#     for line in restaurant_name_raw.split('\n'):
#         line = line.strip()
#     # Skip empty lines and lines that look like explanations
#         if not line or any(word in line.lower() for word in [
#             "need to", "where do i start", "cuisine", "history", "draw from", "want a name", "sounds", "inviting"
#         ]):
#             continue
#     # If the line is short and doesn't look like a sentence, take it as the name
#         if len(line.split()) <= 6 and line[0].isalpha():
#             first_name = line
#             break
#     if not first_name:
#         # fallback: just use the first non-empty line
#         for line in restaurant_name_raw.split('\n'):
#             if line.strip():
#                 first_name = line.strip()
#                 break

#     if not cuisine:
#         return None
    
#     # print("Restaurant Name:", first_name)

# # --- Get menu items for this name ---
#     menu_items_raw = food_item_chain.run({"restaurant_name": first_name})

# # Extract only the first comma-separated list from the output
#     menu_items = None
#     for line in menu_items_raw.split('\n'):
#         line = line.strip()
#     # Only accept lines with at least 4 commas and no periods (to avoid sentences)
#         if line.count(',') >= 4 and '.' not in line:
#             menu_items = line
#             break
#     if not menu_items:
#     # Fallback: try to find a comma-separated list anywhere in the text
#         match = re.search(r'([A-Za-z\s\-]+,\s*[A-Za-z\s\-]+(?:,\s*[A-Za-z\s\-]+){4,})', menu_items_raw)
#         if match:
#             menu_items = match.group(1).strip()
#         else:
#         # fallback: just use the last non-empty line
#             lines = [l.strip() for l in menu_items_raw.split('\n') if l.strip()]
#             menu_items = lines[-1] if lines else ""

#     return {
#             "restaurant_name": f"{first_name}",
#             "menu_items": menu_items
#     }

#     # # Placeholder for the actual name generation logic
#     # # This could be a call to an LLM or a predefined list of names
#     # return {
#     #     "restaurant_name" : "curry delight",
#     #     "menu_items": "Curry Chicken, Vegetable Biryani, Paneer Tikka, Naan Bread, Mango Lassi"
        
#     # }