import paypalrestsdk
from distributed.http.utils import redirect
from django.http import HttpResponse, HttpResponseRedirect
from rest_framework.views import APIView
from rest_framework.response import Response


class PaypalImpl(APIView):

    def post(sel, request):

        paypalrestsdk.configure({
      "mode": "sandbox",
      "client_id": "AfGKGVKuPojlieDTHam8798TkYU5drx6FZqr9Ze28YP_2hnT6QrVT5x0DC3MCMEzfkFbs-nftTBDLq-t",
      "client_secret": "EGgNbRSdI_C3wICQWfA4r36RYNK8UL4BgBopmlGnMW1Lw9DVt85MF3uV0KoP0LOLYERTUoP7hiIcCgmU" })

        payment = paypalrestsdk.Payment({
            "intent": "sale",
            "payer": {
                "payment_method": "paypal"},
            "redirect_urls": {
                "return_url": "http://localhost:8000/api/paypal/pay",
                "cancel_url": "http://localhost:8000/api/paypal/cancel"},
            "transactions": [{
                "amount": {
                    "total": request.data['total'],
                    "currency": request.data['currency']},
                "description": "payment description"}]})

        if payment.create():
            print("Payment created successfully")
            for link in payment.links:
                if link.rel == "approval_url":
                    approval_url = str(link.href)
                    print("Redirect for approval: %s" % (approval_url))
                    # return HttpResponseRedirect(approval_url)
                    return Response(approval_url)
        else:
            print(payment.error)
            # return HttpResponse("支付失败")
            return Response({'msg': 'save failure'})


    def get(self, request):

        paymentid = request.GET.get("paymentId")
        payerid = request.GET.get("PayerID")
        payment = paypalrestsdk.Payment.find(paymentid)

        if payment.execute({"payer_id": payerid}):
            print("Payment execute successfully")




            return HttpResponse("successfully")
        else:
            print(payment.error)
            return HttpResponse("fail")

        # payment = paypalrestsdk.Payment.find("订单号")
        print(payment)

