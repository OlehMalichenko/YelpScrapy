import json
import re
from bs4 import BeautifulSoup
from .util import KeysForJsonDict as Key


def clear_script_string(st: str):
   start_index = st.find('{')
   end_index = st.rfind('}')
   if start_index == -1 or end_index == -1:
      return None
   return st[start_index:end_index+1]


def get_script_data_from_(response_text):
    bs_obj = BeautifulSoup(markup=response_text,
                           features='html.parser')
    body = bs_obj.find('body')
    return body.find(name='script',
                     attrs={'type': 'application/json',
                            'data-hypernova-key': True})


def make_dict_from_(response_text):
    script_data = get_script_data_from_(response_text)
    try:
        app_script_text = str(script_data.contents[0].string.extract())
        app_text = clear_script_string(app_script_text)
    except Exception as e:
        print(e)
        return None
    else:
        try:
            return json.loads(app_text)
        except Exception as e:
            print(e)
            return None


def get_the_server_modules_list_in_(json_dict):
    try:
        return True, json_dict[Key.modules_1][Key.modules_2][Key.modules_3][Key.modules_4]
    except:
        return False, [Key.modules_1, Key.modules_2, Key.modules_3, Key.modules_4]


def find_component_for_(key_component, server_modules_list):
    for s_module in server_modules_list:
        try:
            if s_module[Key.component_key] == key_component:
                return s_module[Key.props]
        except:
            continue
    return None


def get_site(action_buttons):
    try:
        return action_buttons[Key.url_step1][Key.url_step2]
    except:
        return ''


def get_address_telephone_image(json_dict):
    address = dict.fromkeys(['streetAddress', 'addressLocality', 'addressRegion', 'postalCode', 'addressCountry'], '')
    tel = ''
    image = ''
    try:
        scripts_list = json_dict[Key.address_step1][Key.address_step2][Key.address_step3]
    except:
        pass
    else:
        for script in scripts_list:
            script = str(script)
            if script.find('address') != -1 and script.find('telephone') != -1:
                ind1 = script.find('{')
                ind2 = script.find('}<')+1
                script_json = script[ind1: ind2]
                try:
                    script_dict = json.loads(script_json)
                except:
                    pass
                else:
                    try:
                        tel = script_dict['telephone']
                    except:
                        pass
                    try:
                        address.update(script_dict['address'])
                    except:
                        pass
                    try:
                        image = script_dict['image']
                    except:
                        pass
    finally:
        return address, tel, image


def get_email(json_dict):
    try:
        email = json_dict[Key.email_step1][Key.email_step2][Key.email_step3][Key.email_step4][Key.email_step5]
        return email if email else ''
    except:
        return ''


def get_bizid(json_dict):
    try:
        return json_dict[Key.bizid_step1][Key.bizid_step2][Key.bizid_step3]
    except:
        return ''


def get_amenities(json_dict):
    result = []
    try:
        amenities_list = json_dict[Key.amenities_step1][Key.amenities_step2][Key.amenities_step3][Key.amenities_step4][
            Key.amenities_step5]
    except:
        return []
    for element in amenities_list:
        try:
            t: str = element[Key.title_amenities]
            l: str = element[Key.label_amenities]
            if l.lower() == 'yes':
                result.append(t)
            else:
                tl = t + ' - ' + l
                result.append(tl)
        except:
            continue
    return result


def get_hours(json_dict):
    try:
        hours_list = json_dict[Key.hours_step1][Key.hours_step2][Key.hours_step3][Key.hours_step4][Key.hours_step5][
            0].values()
        return ', '.join(hours_list)
    except:
        return ''


def get_about_biz(json_dict):
    try:
        about_biz_dict = json_dict[Key.aboutbiz_step1][Key.aboutbiz_step2][Key.aboutbiz_step3]
    except:
        return ''

    result_list = []
    keys = [Key.specialties_text, Key.year_established, Key.history_text, Key.bio_text, Key.owner_name, Key.owner_role]
    for key in keys:
        try:
            result_list.append(about_biz_dict[key])
        except:
            continue

    return '  '.join(list(filter(None,result_list)))


def get_url(url: str):
    return url.replace('m.yelp', 'www.yelp')



# ==============ALTERNATIVES WAYS================== #
def get_city_state(action_buttons):
    city = ''
    state = ''
    try:
        city = action_buttons[Key.city_state_step1][Key.city_state_step2][Key.city]
    except:
        pass
    try:
        state = action_buttons[Key.city_state_step1][Key.city_state_step2][Key.state]
    except:
        pass
    return city, state

def get_country(json_dict):
    try:
        return json_dict[Key.country_step1][Key.country_step2][Key.country_step3][Key.country_step4][1]
    except:
        return ''

def get_street_zip_tel(standart_action_links):
    street = ''
    zip = ''
    tel = ''
    action_links = standart_action_links.get(Key.action_links, None)
    if action_links:
        for action_element in action_links:
            if action_element.get(Key.sitrep) == Key.sitrep_direction:
                street = action_element.get(Key.label)
                try:
                    city_state_zip = action_element.get(Key.helper_text)[0]
                    r_ind = city_state_zip.rfind(' ')
                    zip = city_state_zip[r_ind + 1:]
                except:
                    pass
            if action_element.get(Key.sitrep) == Key.sitrep_phone:
                try:
                    tel = action_element.get(Key.link_phone).replace('tel:', '')
                except:
                    pass
    return street, zip, tel

def get_img_link_from_(photo_grid):
    media_list = photo_grid.get(Key.media, None)
    if media_list:
        img_links_list = []
        for media_element in media_list:
            img_links_list.append(media_element.get(Key.key_img_link, None))
        return list(filter(None, img_links_list))
    return []



