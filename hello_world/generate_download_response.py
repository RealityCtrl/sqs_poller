def get_response(file_list_helper, url_helper):
    file_list = file_list_helper.get_file_list_with_location()
    for file_dict in file_list:
        url = url_helper.get_download_url(file_dict)
        file_dict["Url"] = url
    return file_list
