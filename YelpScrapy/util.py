import csv
import os
from random import choice


class KeysForJsonDict():
    modules_1 = 'legacyProps'
    modules_2 = 'props'
    modules_3 = 'modules'
    modules_4 = 'serverModules'
    component_key = 'component'

    component_infobox_name = 'InfoBox'
    name = 'name'
    rating = 'rating'
    review_count = 'reviewCount'
    categories = 'categories'

    component_photogrid_name = 'PhotoGrid'
    media = 'media'
    key_img_link = 'srcUrl'

    component_standartactionlinks_name = 'StandardActionLinks'
    action_links = 'actionLinks'
    sitrep = 'sitrepChannel'
    sitrep_direction = 'biz_directions'
    sitrep_phone = 'biz_phone_number'
    label = 'label'
    link_phone = 'link'
    helper_text = 'helperTextList'

    component_actionbuttons_name = 'ActionButtons'
    url_step1 = 'websiteUrl'
    url_step2 = 'displayUrl'
    city_state_step1 = 'syndicationTrackingProps'
    city_state_step2 = 'thirdPartyLeadsConfig'
    city = 'city'
    state = 'state'

    country_step1 = 'gaConfig'
    country_step2 = 'dimensions'
    country_step3 = 'm'
    country_step4 = 'content_country'

    address_step1 = 'legacyProps'
    address_step2 = 'props'
    address_step3 = 'headTags'

    email_step1 = 'legacyProps'
    email_step2 = 'props'
    email_step3 = 'trackingPixelsProps'
    email_step4 = 'liverampTrackingProps'
    email_step5 = 'encryptedEmail'



    bizid_step1 = 'legacyProps'
    bizid_step2 = 'props'
    bizid_step3 = 'bizId'

    amenities_step1 = 'legacyProps'
    amenities_step2 = 'props'
    amenities_step3 = 'moreInfoProps'
    amenities_step4 = 'bizInfo'
    amenities_step5 = 'bizAttributes'
    title_amenities = 'title'
    label_amenities = 'label'

    hours_step1 = 'legacyProps'
    hours_step2 = 'props'
    hours_step3 = 'moreInfoProps'
    hours_step4 = 'bizInfo'
    hours_step5 = 'bizHours'

    aboutbiz_step1 = 'legacyProps'
    aboutbiz_step2 = 'props'
    aboutbiz_step3 = 'fromThisBizProps'
    specialties_text = 'specialtiesText'
    year_established = 'yearEstablished'
    history_text = 'historyText'
    bio_text = 'bioText'
    owner_name = 'ownerName'
    owner_role = 'ownerRole'

    props = 'props'


def get_random_user_agent():
    user_agents = [
        'Mozilla/5.0 (iPhone; CPU iPhone OS 10_3_1 like Mac OS X) AppleWebKit/603.1.30 (KHTML, like Gecko) Version/10.0 Mobile/14E304 Safari/602.1',
        'Mozilla/5.0 (Linux; U; Android 4.4.2; en-us; SCH-I535 Build/KOT49H) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30',
        'Mozilla/5.0 (Android 7.0; Mobile; rv:54.0) Gecko/54.0 Firefox/54.0',
        'Mozilla/5.0 (Linux; Android 7.0; SM-G930V Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 Mobile Safari/537.36']
    return choice(user_agents)


def url_preparation(url: str):
    ind = url.find('yelp.com/biz/')
    if ind == -1:
        return None
    return f'https://m.{url[ind:]}'


def read_urls_from_file_csv(file: str):
    urls = []
    if not os.path.exists(file):
        return urls
    with open(file, 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            url = url_preparation(row['url'])
            if url:
                urls.append(url)
    return urls

