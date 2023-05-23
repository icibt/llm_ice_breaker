import os
import requests


def scrape_linkedin_profile(linkedin_profile_url: str):
    # https://gist.githubusercontent.com/icibt/6db388852ff5a306daeaeac4919f0018/raw/08ce88e81058186da796aea15346cdc78d0d84bb/testData.json
    """
    scrape information from LinkedIn profiles,
    Manually scrape the information from the LinkedIn profile
    """

    api_endpoint = "https://nubela.co/proxycurl/api/v2/linkedin"
    api_key = os.environ.get("PROXYCURL_API_KEY")
    header_dic = {"Authorization": "Bearer " + api_key}
    params = {
        "url": linkedin_profile_url,
    }
    response = requests.get(api_endpoint, params=params, headers=header_dic)

    data = response.json()
    data = {
        k: v
        for k, v in data.items()
        if v not in ([], "", "", None)
        and k not in ["people_also_viewed", "certifications"]
    }

    if data.get("groups"):
        for group_dict in data.get("groups"):
            group_dict.pop("profile_pic_url")

    return data

    return response
