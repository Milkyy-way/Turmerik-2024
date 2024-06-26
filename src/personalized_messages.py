# Required Libraries
from imports import *
from dotenv import load_dotenv

load_dotenv("../config/config.env")

# Set up OpenAI API key
openai.api_key = os.getenv("OPENAI_API_KEY")

# Load the DataFrame with sentiment scores
df = pd.read_csv("../data/scores.csv")

# Filtering 4 and 5 scores
filtered_df = df[df["Score"].isin([4, 5])]

# List to store personalized messages generated by OpenAI
personalized_messages = []

# Iterate over the first 2 rows of filtered_df
for idx, row in filtered_df.iterrows():
    comment = row["Comment_Body"]
    
    # Create a prompt for personalized message
    prompt = (
        "There is a clinical trial happening at Turmeric. Generate a personalized message to invite the participant "
        f"who has commented the following on Reddit to the clinical trial. Comment: {comment}"
    )

    # Call OpenAI to generate the personalized message
    response = openai.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )

    try:
        if len(response.choices) > 0:
            first_choice = response.choices[0]
            personalized_message = first_choice.message.content
            
            # Store the personalized message along with the index
            personalized_messages.append((idx, personalized_message))
        else:
            personalized_message = "No message generated"
    
    except (AttributeError, IndexError) as e:
        print(f"Error extracting personalized message: {e}")

# Convert the list of personalized messages to a DataFrame
personalized_df = pd.DataFrame(personalized_messages, columns=["Index", "Status"])

# Add the new "Status" column to filtered_df
filtered_df = filtered_df.merge(personalized_df, left_index=True, right_on="Index")

# Save the updated DataFrame to a CSV file
filtered_df.to_csv("../data/personalized_messages.csv", index=False)

# Output the updated DataFrame
print(filtered_df)
