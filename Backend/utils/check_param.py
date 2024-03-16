import re, json
from functools import wraps
from django.http import JsonResponse

def check_params(param_dict):
    def decorator(view_func):
        @wraps(view_func)
        def wrapped_view(self, request, *args, **kwargs):
            missing_required_params = []
            invalid_params = []
            parsed_params = {}

            for param, config in param_dict.items():
                value = request.data.get(param) if not request.data.get(param) == None else request.GET.get(param)

                # 获取参数的校验规则和必填性质
                regex = config.get('re')
                required = config.get('required', True)
                default = config.get('default', None)

                if value is None or len(str(value)) == 0:
                    if required:
                        missing_required_params.append(param)
                    elif default != None:
                        parsed_params[param] = default
                elif value and regex and not re.match(regex, str(value)):
                    invalid_params.append(param)
                else:
                    if config.get('type') == 'int': 
                        try: 
                            parsed_param = int(value)
                            if 'min' in config and parsed_param < config['min']:
                                invalid_params.append(param)
                            if 'max' in config and parsed_param > config['max']:
                                invalid_params.append(param)
                            parsed_params[param] = parsed_param
                        except: 
                            invalid_params.append(param)
                    elif config.get('type') == 'float': 
                        try: 
                            parsed_param = float(value)
                            if 'min' in config and parsed_param < config['min']:
                                invalid_params.append(param)
                            if 'max' in config and parsed_param > config['max']:
                                invalid_params.append(param)
                            parsed_params[param] = parsed_param
                        except: 
                            invalid_params.append(param)
                    elif config.get('type') == 'boolean': 
                        try: 
                            parsed_params[param] = bool(int(value))
                        except: 
                            invalid_params.append(param)
                    elif config.get('type') == 'json': 
                        try: 
                            parsed_params[param] = json.loads(value)
                        except: 
                            invalid_params.append(param)
                    else:
                        parsed_params[param] = value

            if missing_required_params:
                # 处理必填参数的缺失
                return JsonResponse({
                    'status': 1, 
                    'msg': "Missing params: {}".format(", ".join(missing_required_params)),
                })

            if invalid_params:
                # 处理参数的非法情况
                return JsonResponse({
                    'status': 1, 
                    'msg': "Invalid params: {}".format(", ".join(invalid_params)),
                })

            kwargs['params'] = parsed_params  # 将解析出来的参数传递给视图函数

            return view_func(self, request, *args, **kwargs)

        return wrapped_view

    return decorator
