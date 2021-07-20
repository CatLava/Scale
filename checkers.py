def occlusion_check(occ, curr):
    clean = occ['response']['annotations']
    for item in clean:
        cover = item['attributes']['occlusion']
        cover = int(cover.replace('%', ''))
        if cover >= 50:
            curr.append(f" WARNING: High occlusion for {item['uuid']}")
            #print(curr)
    return curr


# This will check time spent on task if it is possible
# If time is under a certain threshold
def time_check(task, curr):
    check = task['customer_audit_time_secs']
    if check < 30:
        curr.append(f" NOTICE: suspect time {check}")
    return curr

'''This checks if the Not_Applicable tag is only for non-visible face label'''
def background_NA_check(task, curr):
    check = task['response']['annotations']
    for box in check:
        label = box['label']
        color = box['attributes']['background_color']
        if label != 'non_visible_face' and color == 'not_applicable':
            #print(f"WARNING: invalid color description for {label}")
            curr.append(f" ERROR: invalid color description for {label}")
    return curr