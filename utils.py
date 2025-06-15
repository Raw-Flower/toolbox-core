from django.db.models import Q

def get_query_conditions(data,filters_dict):
    query_filters = Q()
    for k,v in data.items():
        if v:
            filter_spec = filters_dict.get(k)
            if isinstance(filter_spec,list):#Check if filter_spec has a list or not 
                field_name, filter_type = filter_spec[0], filter_spec[1] #Assign the values
            else:
                field_name, filter_type = k, filter_spec
            query_condition = f'{field_name}__{filter_type}' #Prepare query conditions based on filter_spec
            query_filters &= Q(**{query_condition:v}) #Send as argument the query condition(dict)
    return query_filters