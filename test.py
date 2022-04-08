# Streamlit Timeline Component Example

import streamlit as st
from streamlit_timeline import timeline

# use full page width
st.set_page_config(page_title="Timeline Example", layout="wide")

# load data
# with open('example.json', "r") as f:
#     data = f.read()

data = {

    # Starting slide
    "title": {
        "media": {
            "url": "https://github.com/zeyalt/PM-Lee-Covid19-Speeches/blob/master/pm_lee.jpg?raw=true",
            # "caption": " <a target=\"_blank\" href=''>credits</a>",
            "credit": "Source: Prime Minister's Office"
        },
        "text": {
            "headline": "Singapore's<br>COVID-19 Journey",
            "text": "Since COVID-19 struck Singapore in January 2020,<br>PM Lee has addressed the nation several times. Each<br>speech reflected the state of the pandemic as well as<br>measures taken by the Singapore Government. This<br>timeline summarises the journey using key phrases from<br>PM Lee's speeches."
        }
    },

    # Subsequent slides
    "events": [
        {
        # Slide 1
        "media": {
            "url": "https://github.com/zeyalt/PM-Lee-Covid19-Speeches/blob/master/Images/phrasecloud_2020-02-08.png?raw=true",
            "credit": "Source: Prime Minister's Office Singapore (<a target=\"_blank\" href='https://www.pmo.gov.sg/Newsroom/PM-Lee-Hsien-Loong-on-the-Novel-Coronavirus-nCoV-Situation-in-Singapore-on-8-February-2020'>Link to speech</a>)"
        },
        "start_date": {
            "year": "2020",
            "month": "2",
            "day": "8",
            # "display_date": "HH-MM-YYYY"
        },
        "text": {
            "headline": "The Beginning", 
            "text": " "
        }
        },
        {
        # Slide 2
        "media": {
            "url": "https://github.com/zeyalt/PM-Lee-Covid19-Speeches/blob/master/Images/phrasecloud_2020-03-12.png?raw=true",
            "credit": "Source: Prime Minister's Office Singapore (<a target=\"_blank\" href='https://www.pmo.gov.sg/Newsroom/PM-Lee-remarks-COVID-19-Outbreak-12-Mar-2020'>Link to speech</a>)"
        },
        "start_date": {
            "year": "2020",
            "month": "3",
            "day":"12"
        },
        "text": {
            "headline": "Staying Resilient",
            "text": '<i>"Singapore’s response has received international accolades. Underlying this is the social and psychological resilience of our people. What makes Singapore different from other countries is that we have confidence in each other, we feel that we are all in this together, and we do not leave anyone behind. This is SG United, we are SG United."'
        }
        },
        {
        # Slide 3
        "media": {
            "url": "https://github.com/zeyalt/PM-Lee-Covid19-Speeches/blob/master/Images/phrasecloud_2020-04-03.png?raw=true",
            "credit": "Source: Prime Minister's Office Singapore (<a target=\"_blank\" href='https://www.pmo.gov.sg/Newsroom/PM-Lee-Hsien-Loong-on-the-COVID19-situation-in-Singapore-on-3-April-2020'>Link to speech</a>)"
        },
        "start_date": {
            "year": "2020",
            "month":"4",
            "day": "3"
        },
        "text": {
            "headline": "Breaking The Circuit",
            "text": '<i>"We have decided that instead of tightening incrementally over the next few weeks, we should make a decisive move now to pre-empt escalating infections. We will therefore impose significantly stricter measures. This is like a circuit breaker.</i>"'
        }
        },
        {
        # Slide 4
        "media": {
            "url": "https://github.com/zeyalt/PM-Lee-Covid19-Speeches/blob/master/Images/phrasecloud_2020-04-10.png?raw=true",
            "credit": "Source: Prime Minister's Office Singapore (<a target=\"_blank\" href='https://www.pmo.gov.sg/Newsroom/PM-Lee-Hsien-Loong-on-the-COVID-19-situation-in-Singapore-on-10-April-2020'>Link to speech</a>)"
        },
        "start_date": {
            "year": "2020",
            "month":"4",
            "day": "10"
        },
        "text": {
            "headline": "Outbreak in Foreign Worker Dormitories",
            "text": '<i>"The next few weeks will be tough. I will speak to you like this from time to time. So that you know what the real situation is, what we are thinking, what you can expect and how you can play your part to fight this virus. The situation will get worse before it gets better, but we have to get through this, before the sun comes out and shines on us again."</i>',
            # "media": {
            #     "url": "https://github.com/zeyalt/PM-Lee-Covid19-Speeches/blob/master/Images/dormitory.jpg?raw=true",
            #     "credit": "Source: Prime Minister's Office Singapore (<a target=\"_blank\" href='https://www.pmo.gov.sg/Newsroom/PM-Lee-Hsien-Loong-on-the-COVID-19-situation-in-Singapore-on-10-April-2020'>Link to speech</a>)"
            # }
        }
        },
        {
        # Slide 5
        "media": {
            "url": "https://github.com/zeyalt/PM-Lee-Covid19-Speeches/blob/master/Images/phrasecloud_2020-04-21.png?raw=true",
            "credit": "Source: Prime Minister's Office Singapore (<a target=\"_blank\" href='https://www.pmo.gov.sg/Newsroom/PM-Lee-Hsien-Loong-address-COVID-19-21-Apr'>Link to speech</a>)"
        },
        "start_date": {
            "year": "2020",
            "month":"4",
            "day": "21"
        },
        "text": {
            "headline": "Extending The Circuit Breaker",
            "text": '<i>"To our migrant workers, let me emphasise again: we will care for you, just like we care for Singaporeans. We thank you for your cooperation during this difficult period. We will look after your health, your welfare and your livelihood. We will work with your employers to make sure that you get paid, and you can send money home. And we will help you stay in touch with friends and family."</i>'
        }
        },
        {
        # Slide 6
        "media": {
            "url": "https://github.com/zeyalt/PM-Lee-Covid19-Speeches/blob/master/Images/phrasecloud_2020-06-07.png?raw=true",
            "credit": "Source: Prime Minister's Office Singapore (<a target=\"_blank\" href='https://www.pmo.gov.sg/Newsroom/National-Broadcast-PM-Lee-Hsien-Loong-COVID-19'>Link to speech</a>)"
        },
        "start_date": {
            "year": "2020",
            "month":"6",
            "day": "7"
        },
        "text": {
            "headline": "Overcoming Crisis<br>of a Generation",
            "text": '<i>"For our plans to succeed, for our hopes and dreams to come true, we need one final ingredient: the unity and resilience of our people. Once in a while, nations and peoples are severely tested, as we are now. Some buckle under pressure and emerge from crisis diminished. Others grow more determined as they face fearful odds, discover reserves of strength in themselves, and emerge from crisis transfigured, renewed. And that has been our Singapore story: in crises, we have never failed to wrest opportunity from danger."</i>'
        }
        },
        {
        # Slide 7
        "media": {
            "url": "https://github.com/zeyalt/PM-Lee-Covid19-Speeches/blob/master/Images/phrasecloud_2020-12-14.png?raw=true",
            "credit": "Source: Prime Minister's Office Singapore (<a target=\"_blank\" href='https://www.pmo.gov.sg/Newsroom/PM-Lee-Hsien-Loong-on-the-COVID-19-situation-in-Singapore-on-14-December-2020'>Link to speech</a>)"
        },
        "start_date": {
            "year": "2020",
            "month":"12",
            "day": "14"
        },
        "text": {
            "headline": "Easing Up Cautiously",
            "text": '<i>"Now, our defences against COVID-19 are much stronger. We have steadily built up our testing capacities and procedures. We introduced Rostered Routine Testing of higher risk groups. We started using Antigen Rapid Tests, to resume larger gatherings and events safely. We also beefed up our contact tracing capabilities for example, expanding our SafeEntry and TraceTogether programmes, and distributing TraceTogether tokens."</i>'
        }
        },
        {
        # Slide 8
        "media": {
            "url": "https://github.com/zeyalt/PM-Lee-Covid19-Speeches/blob/master/Images/phrasecloud_2021-05-31.png?raw=true",
            "credit": "Source: Prime Minister's Office Singapore (<a target=\"_blank\" href='https://www.pmo.gov.sg/Newsroom/PM-Lee-Hsien-Loong-COVID-19-New-Normal-31-May-2021'>Link to speech</a>)"
        },
        "start_date": {
            "year": "2021",
            "month":"5",
            "day": "31"
        },
        "text": {
            "headline": "Test, Trace and Vaccinate",
            "text": '<i>"We are now dealing with the B.1.617.2 variant, which was first detected in India and is now in over 50 countries. More variants will inevitably emerge, and we will have to deal with them too. What does a more infectious virus mean for our fight against COVID-19? It implies that we must continually adjust our strategies, and raise our game to keep COVID-19 under control. Specifically, there are three things that we have to do more of, and do faster, testing, contact tracing, and vaccination."</i>'
        }
        },
        {
        # Slide 9
        "media": {
            "url": "https://github.com/zeyalt/PM-Lee-Covid19-Speeches/blob/master/Images/phrasecloud_2021-10-09.png?raw=true",
            "credit": "Source: Prime Minister's Office Singapore (<a target=\"_blank\" href='https://www.pmo.gov.sg/Newsroom/Update-on-the-COVID-19-Situation-In-Singapore-by-Prime-Minister-Lee-Hsien-Loong-on-9-October'>Link to speech</a>)"
        },
        "start_date": {
            "year": "2021",
            "month":"10",
            "day": "9"
        },
        "text": {
            "headline": "Living with COVID-19",
            "text": '<i>"That is why we are shifting to relying heavily on Home Recovery. It will be the norm for COVID-19 cases. You can get well in a familiar home setting, without the stress and bother of admitting yourself into a care facility. If most of us can recover at home, it will greatly ease the strain on our hospitals, doctors and nurses. Next, since COVID-19 has become a manageable disease, we should now drastically simplify our health protocols. No more complicated flow charts. People must be clear what to do if they test positive, or if they come into contact with someone who is infected. "</i>'
        }
        },
        {
        # Slide 10
        "media": {
            "url": "https://github.com/zeyalt/PM-Lee-Covid19-Speeches/blob/master/Images/phrasecloud_2022-03-24.png?raw=true",
            "credit": "Source: Prime Minister's Office Singapore (<a target=\"_blank\" href='https://www.pmo.gov.sg/Newsroom/PM-Lee-Hsien-Loong-on-COVID-19-A-New-Phase-on-24-Mar-2022'>Link to speech</a>)"
        },
        "start_date": {
            "year": "2022",
            "month":"3",
            "day": "24"
        },
        "text": {
            "headline": "A Turning Point",
            "text": '<i>"Taking all things into consideration, we believe that we are now ready to take a decisive step forward towards living with COVID-19. Resume more normal lives, enjoy larger gatherings of family and friends, go outdoors without masks, or reunite with loved ones abroad. But do not throw all caution to the wind. Each one of us must still play our part."</i>'
        }
        },
    ]
    }

# print(data)

# render timeline
timeline(data, height=800)