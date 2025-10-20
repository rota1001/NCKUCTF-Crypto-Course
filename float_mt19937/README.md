
```cpp
// https://github.com/python/cpython/blob/11a5fc82381308f0b6060b8c06af89fd197516e1/Modules/_randommodule.c#L187
static PyObject *
_random_Random_random_impl(RandomObject *self)
/*[clinic end generated code: output=117ff99ee53d755c input=26492e52d26e8b7b]*/
{
    uint32_t a=genrand_uint32(self)>>5, b=genrand_uint32(self)>>6;
    return PyFloat_FromDouble((a*67108864.0+b)*(1.0/9007199254740992.0));
}
```